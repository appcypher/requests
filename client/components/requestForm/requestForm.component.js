import ko from 'knockout';
import 'knockout-postbox';
import $ from 'jquery';
import { suggestionBoxEvents } from '../../events/animations';
import template from './requestForm.html';
import './requestForm.scss';
import dropdownIcon from '../../assets/icons/dropdown.svg';
import titleIcon from '../../assets/icons/title.svg';
import clientIcon from '../../assets/icons/client.svg';
import priorityIcon from '../../assets/icons/priority.svg';
import labelIcon from '../../assets/icons/label.svg';
import dateIcon from '../../assets/icons/date.svg';
import descriptionIcon from '../../assets/icons/description.svg';
import {
  showError,
  showOK,
  showLoader,
  hideLoader,
  hideForm,
} from '../app/app.component';
import { postRequest } from '../../http';

class ViewModel {
  constructor() {
    // Inline SVGs.
    this.dropdownIcon = dropdownIcon;
    this.titleIcon = titleIcon;
    this.clientIcon = clientIcon;
    this.priorityIcon = priorityIcon;
    this.labelIcon = labelIcon;
    this.dateIcon = dateIcon;
    this.descriptionIcon = descriptionIcon;
    this.staffId = 1;
    this.clientId = 0;
    // Temporarily hard-coded.
    this.clients = ko.observableArray([
      { name: 'Client A', id: 1 },
      { name: 'Client B', id: 2 },
      { name: 'Client C', id: 3 },
    ]);
    this.productAreas = ko.observableArray([
      { name: 'POLICIES' },
      { name: 'BILLING' },
      { name: 'CLAIMS' },
      { name: 'REPORTS' },
    ]);

    // Observables
    this.title = ko.observable('');
    this.client = ko.observable('');
    this.priority = ko.observable('');
    this.productArea = ko.observable('');
    this.dueDate = ko.observable('');
    this.description = ko.observable('');
    this.clientList = ko.observableArray();
    this.newRequestList = ko.observable().publishOn('newRequestList');

    // Autosuggestion timers.
    this.clientSuggestionsTimeout = null;
    this.categorySuggestionsTimeout = null;

    // Subscriptions
    this.client.subscribe((newValue) => {
      const selector = '.request-form__client > .request-form__select';
      suggestionBoxEvents(selector, this.clientSuggestionsTimeout);
    });

    this.productArea.subscribe((newValue) => {
      const selector = '.request-form__area > .request-form__select';
      suggestionBoxEvents(selector, this.categorySuggestionsTimeout);
    });
  }

  selectClient = (data) => {
    this.clientId = data.id;
    this.client(data.name);
    $('.request-form__client > .request-form__select').hide();
  }

  selectProductArea = (data) => {
    this.productArea(data.name);
    $('.request-form__area > .request-form__select').hide();
  }

  // Submits the form.
  submit = () => {
    const data = {
      title: this.title(),
      priority: this.priority(),
      product_area: this.productArea().toUpperCase(),
      client_id: this.clientId,
      staff_id: this.staffId,
      target_date: `${this.dueDate()}T00:00`,
      description: this.description(),
    };

    showLoader();

    postRequest(data)
      .then((response) => {
        hideForm();
        hideLoader();
        showOK(response.data.message);
        this.newRequestList(response);
      })
      .catch((error) => {
        hideLoader();
        showError(error.response.data.message);
      });
  }
}

ko.components.register('request-form', { viewModel: ViewModel, template });
