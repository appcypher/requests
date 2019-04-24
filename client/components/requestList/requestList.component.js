import ko from 'knockout';
import 'knockout-postbox';
import moment from 'moment';
import template from './requestList.html';
import './requestList.scss';
import searchIcon from '../../assets/icons/search.svg';
import dropdownIcon from '../../assets/icons/dropdown.svg';
import checkIcon from '../../assets/icons/check.svg';
import plusIcon from '../../assets/icons/plus.svg';
import { getRequests, getRequest } from '../../http';
import {
  showError, showLoader, hideLoader, getPriorityColor,
  formatDate, formatTime,
} from '../app/app.component';
import avatarUrl from '../../assets/icons/placeholder.png';

class ViewModel {
  constructor() {
    // Inline SVGs.
    this.searchIcon = searchIcon;
    this.dropdownIcon = dropdownIcon;
    this.checkIcon = checkIcon;
    this.plusIcon = plusIcon;

    // Observables
    this.requests = ko.observableArray([]);
    this.requestsByDays = ko.observableArray([]);
    this.newRequestDetails = ko.observable().publishOn('newRequestDetails');
    this.newRequestList = ko.observable().subscribeTo('newRequestList');

    ko.computed({
      owner: this,
      read: () => {
        const requests = ViewModel.groupRequests(this.requests);
        this.requestsByDays(requests);
        if (requests.length > 0) {
          this.selectRequest(requests[0].requests[0]);
        }
      },
    });

    ko.computed(() => {
      this.newRequestList();
      this.getRequests();
    });

    this.getRequests();
  }

  // Get all the requests.
  getRequests = () => {
    // Show the loader.
    showLoader();

    getRequests()
      .then((response) => {
        hideLoader();
        this.requests(response.data.data);
      })
      .catch((error) => {
        hideLoader();
        showError(error.response.data.message);
      });
  }

  getPriorityColor = priority => getPriorityColor(priority)

  // Selects a request on the list an opens the details.
  selectRequest = ({ id }) => {
    this.newRequestDetails({ id, message: '' });
  }

  // Groups and sorts by date.
  static groupRequests = (requests) => {
    // First group requests into dates.
    const requestsByDay = requests().reduce((groupedRequests, request) => {
      const date = request.created_at.slice(0, 10);
      if (!groupedRequests[date]) {
        // eslint-disable-next-line no-param-reassign
        groupedRequests[date] = { date: request.created_at, requests: [request] };
      } else {
        groupedRequests[date].requests.push(request);
      }
      return groupedRequests;
    }, {});

    // Sort chronologically.
    const orderedRequests = [];
    Object.keys(requestsByDay).sort().reverse().forEach((key) => {
      // Sort entry by date.
      const { date, requests: oldRequests } = requestsByDay[key];
      const sortedRequests = oldRequests.sort(
        (a, b) => new Date(a.created_at).getTime() - new Date(b.created_at).getTime(),
      ).reverse();

      orderedRequests.push({
        date,
        requests: sortedRequests,
      });
    });

    return orderedRequests;
  }

  // Formats date string.
  formatDate = date => formatDate(date)

  // Formats time string.
  formatTime = date => formatTime(date)

  // Gets placeholder if there is no avatar
  getAvatar = url => url || avatarUrl
}

ko.components.register('request-list', { viewModel: ViewModel, template });
ko.bindingHandlers.css2 = ko.bindingHandlers.css;
