import ko from 'knockout';
import 'knockout-postbox';
import template from './requestList.html';
import './requestList.scss';
import searchIcon from '../../assets/icons/search.svg';
import dropdownIcon from '../../assets/icons/dropdown.svg';
import checkIcon from '../../assets/icons/check.svg';
import plusIcon from '../../assets/icons/plus.svg';
import { getRequests } from '../../http';
import {
  showLoader, hideLoader, getPriorityColor,
  formatDate, formatTime,
} from '../app/app.component';
import { sortToggleSlide, DropdownAnimations } from '../../events/animations';
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
    this.requestsGroupedByClient = ko.observableArray([]);
    this.requestsGroupedByDate = ko.observableArray([]);
    this.groupedByClient = ko.observable(true);
    this.newRequestDetails = ko.observable().publishOn('newRequestDetails');
    this.newRequestList = ko.observable().subscribeTo('newRequestList');

    // Gets and sort the requests first.
    ko.computed({
      owner: this,
      read: () => {
        this.sortRequests();
      },
    });

    // React to changes on requests.
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
      });
  }

  // Gets priority color.
  getPriorityColor = priority => getPriorityColor(priority)

  // Selects a request on the list an opens the details.
  selectRequest = ({ id }) => {
    this.newRequestDetails({ id, message: '' });
  }

  // Toggles sort type.
  toggleSortType = () => {
    // Toggle value
    this.groupedByClient(!this.groupedByClient());

    // Animate toggle.
    sortToggleSlide(this.groupedByClient());

    // Resort request list.
    this.sortRequests();
  }

  // Groups and sorts requests based on sort toggle.
  sortRequests = () => {
    // Group requests.
    if (this.groupedByClient()) {
      this.requestsGroupedByClient(ViewModel.groupRequests(
        this.requests,
        request => request.client.username,
        'client',
        (a, b) => (a.priority > b.priority ? 1 : -1),
      ));

      if (this.requestsGroupedByClient().length > 0 && this.requestsGroupedByDate().length < 1) {
        this.selectRequest(this.requestsGroupedByClient()[0].requests[0]);
      }
    } else {
      this.requestsGroupedByDate(ViewModel.groupRequests(
        this.requests,
        request => request.created_at.slice(0, 10),
        'date',
        (a, b) => new Date(a.created_at).getTime() - new Date(b.created_at).getTime(),
        true,
      ));
    }

    // Register dropdown animation.
    new DropdownAnimations(
      '.request-list__dropdown-icon',
      '.request-list__day',
      '.request-list__entries',
    ).registerAnimations();
  }

  // Groups requests and sorts each subgroup by some criteria.
  static groupRequests = (requests, getKey, keyName, comparator, reverse = false) => {
    // First group requests into dates.
    const groupedRequests = requests().reduce((newRequests, request) => {
      const keyValue = getKey(request);
      if (!newRequests[keyValue]) {
        // eslint-disable-next-line no-param-reassign
        newRequests[keyValue] = { [keyName]: keyValue, requests: [request] };
      } else {
        newRequests[keyValue].requests.push(request);
      }
      return newRequests;
    }, {});

    // Results of requests with ordered subgroup
    const orderedRequests = [];
    let keys;

    // Get keys of grouped requests. Reverse if specified.
    if (reverse) {
      keys = Object.keys(groupedRequests).sort().reverse();
    } else {
      keys = Object.keys(groupedRequests).sort();
    }

    // Iterate over each key and sort subgroup.
    keys.forEach((key) => {
      const oldRequests = groupedRequests[key].requests;
      const keyValue = groupedRequests[key][keyName];

      // Sort entry by comparator.
      let sortedRequests = oldRequests.sort(comparator);

      // Reverse subgroup if specified.
      if (reverse) {
        sortedRequests = sortedRequests.reverse();
      }

      // Push values to new array.
      orderedRequests.push({
        [keyName]: keyValue,
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
