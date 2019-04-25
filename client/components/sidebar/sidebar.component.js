import ko from 'knockout';
import $ from 'jquery';
import template from './sidebar.html';
import './sidebar.scss';
import profileIcon from '../../assets/icons/profile.svg';
import messageIcon from '../../assets/icons/message.svg';
import requestIcon from '../../assets/icons/request.svg';
import calendarIcon from '../../assets/icons/calendar.svg';
import statsIcon from '../../assets/icons/stats.svg';
import { getStaff } from '../../http';
import avatarUrl from '../../assets/icons/placeholder.png';
import {
  hideLoader,
  showLoader,
  showError,
} from '../app/app.component';

class ViewModel {
  constructor() {
    this.profileIcon = profileIcon;
    this.messageIcon = messageIcon;
    this.requestIcon = requestIcon;
    this.calendarIcon = calendarIcon;
    this.statsIcon = statsIcon;

    this.staffId = 1;
    this.staff = ko.observable({ avatar_url: '' });
    this.getStaff();
  }

  // eslint-disable-next-line class-methods-use-this
  reload = () => {
    location.reload();
  }

  // Gets placeholder if there is no avatar
  getAvatar = url => url || avatarUrl

  // Gets the current staff account info.
  getStaff = () => {
    getStaff(this.staffId)
      .then(({ data }) => {
        this.staff(data.data);
      })
      .catch((error) => {
        showError(error);
      });
  }
}

ko.components.register('sidebar', { viewModel: ViewModel, template });
