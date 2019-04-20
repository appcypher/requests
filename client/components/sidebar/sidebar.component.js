import ko from 'knockout';
import $ from 'jquery';
import template from './sidebar.html';
import './sidebar.scss';
import profile from '../../assets/icons/profile.svg';
import message from '../../assets/icons/message.svg';
import request from '../../assets/icons/request.svg';
import calendar from '../../assets/icons/calendar.svg';
import stats from '../../assets/icons/stats.svg';

class ViewModel {
  constructor() {
    this.profile = profile;
    this.message = message;
    this.request = request;
    this.calendar = calendar;
    this.stats = stats;
  }

  // eslint-disable-next-line class-methods-use-this
  reload() {
    location.reload();
  }
}

ko.components.register('sidebar', { viewModel: ViewModel, template });
