import ko from 'knockout';
import 'knockout-postbox';
import template from './requestDetails.html';
import './requestDetails.scss';
import descriptionIcon from '../../assets/icons/description.svg';
import commentIcon from '../../assets/icons/comment.svg';
import dropdownIcon from '../../assets/icons/dropdown.svg';
import {
  getPriorityColor,
  formatDate,
  formatTime,
  showLoader,
  hideLoader,
  showOK,
  showError,
} from '../app/app.component';
import avatarUrl from '../../assets/icons/placeholder.png';
import { postRequestComment, getRequest } from '../../http';
import adjustCommentInput from '../../events/responsiveness';


class ViewModel {
  constructor() {
    this.descriptionIcon = descriptionIcon;
    this.commentIcon = commentIcon;
    this.dropdownIcon = dropdownIcon;
    this.staff_id = 1;

    // Observables.
    this.request = ko.observable({
      id: 0,
      title: 'Loading...',
      description: 'Loading...',
      resolved: true,
      priority: 1,
      avatarUrl: '',
      comments: [],
      product_area: 'BILLING',
      client: {
        username: 'Loading...',
        avatar_url: '',
      },
    });
    this.newRequestDetails = ko.observable({
      id: 0,
      message: '',
    }).syncWith('newRequestDetails');
    this.message = ko.observable('');

    ko.computed(() => {
      showLoader();
      const { id } = this.newRequestDetails();

      if (id) {
        getRequest(id)
          .then(({ data }) => {
            hideLoader();
            this.request(data.data);
            console.log('>>>>>', this.request());
            adjustCommentInput();
          })
          .catch((error) => {
            hideLoader();
            showError(error);
          });
      }
    });
  }

  getPriorityColor = priority => getPriorityColor(priority)

  getStateText = () => (this.request().resolved ? 'Completed' : 'In progress')

  // Formats date string.
  formatDate = date => formatDate(date)

  // Formats time string.
  formatTime = date => formatTime(date)

  // Gets placeholder if there is no avatar
  getAvatar = url => url || avatarUrl

  postComment = ({ request }, event) => {
    // When enter key is pressed.
    if (event.keyCode === 13) {
      const message = this.message();

      // Check if message isn't empty.
      if (message) {
        const { id } = request();
        this.message('');

        showLoader();

        postRequestComment(id, {
          message,
          staff_id: this.staff_id,
        })
          .then((response) => {
            hideLoader();
            this.newRequestDetails({ id, message });
          })
          .catch((error) => {
            hideLoader();
          });
      }
    }
  }
}

ko.components.register('request-details', { viewModel: ViewModel, template });
ko.bindingHandlers.css2 = ko.bindingHandlers.css;
