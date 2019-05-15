import ko from 'knockout';
import $ from 'jquery';
import moment from 'moment';
import template from './app.html';
import './app.scss';
import { toastSlide } from '../../events/animations';

const showError = (message) => {
  let msg = `${message}!`;
  if (typeof message === 'object') {
    Object.entries(message).forEach((errors) => {
      msg = `${errors[0]}: ${errors[1]}`;
    });
  }
  $('.toast').text(msg);
  toastSlide();
};

const showOK = (message) => {
  $('.toast').text(`${message}!`);
  toastSlide();
};

const showLoader = () => {
  $('.popup-container').css({ display: 'flex' });
  $('toast').hide();
  $('.loader').show();
};

const hideLoader = () => {
  $('.popup-container').hide();
  $('.loader').hide();
};

const hideForm = () => {
  $('.request-form__background').hide();
};

const getPriorityColor = (priority) => {
  let color = '#A71C3D';

  if (priority === 1) {
    color = '#0cd920';
  } else if (priority === 2) {
    color = '#078714';
  } else if (priority === 3) {
    color = '#ceba07';
  } else if (priority > 3 && priority <= 8) {
    color = '#A4B200';
  } else if (priority > 8 && priority <= 10) {
    color = '#ed8002';
  } else if (priority > 10 && priority <= 15) {
    color = '#d7a80d';
  }

  return color;
};

// const getPriorityColor = priority => (`lighten(#00FF84, ${priority}%)`);

const formatDate = (date) => {
  let dateString = moment(date).format('DD MMMM YYYY');

  const today = moment();
  const yesterday = moment().subtract(1, 'day');

  if (moment(date).isSame(today, 'day')) {
    dateString = 'Today';
  } else if (moment(date).isSame(yesterday, 'day')) {
    dateString = 'Yesterday';
  }
  return dateString;
};

const formatTime = time => moment(time).format('hh:mm');

ko.components.register('app', { template });

export {
  showError,
  showOK,
  showLoader,
  hideLoader,
  getPriorityColor,
  formatDate,
  formatTime,
  hideForm,
};
