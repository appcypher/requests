import ko from 'knockout';
import $ from 'jquery';
import template from './sidebar.html';
import './sidebar.scss';
import profileIcon from '../../assets/icons/profile.svg';
import messageIcon from '../../assets/icons/message.svg';
import requestIcon from '../../assets/icons/request.svg';
import calendarIcon from '../../assets/icons/calendar.svg';
import statsIcon from '../../assets/icons/stats.svg';

class ViewModel {
  constructor() {
    this.profileIcon = profileIcon;
    this.messageIcon = messageIcon;
    this.requestIcon = requestIcon;
    this.calendarIcon = calendarIcon;
    this.statsIcon = statsIcon;
  }

  // eslint-disable-next-line class-methods-use-this
  reload() {
    location.reload();
  }
}

ko.components.register('sidebar', { viewModel: ViewModel, template });
