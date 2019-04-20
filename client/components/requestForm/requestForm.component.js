import ko from 'knockout';
import template from './requestForm.html';
import './requestForm.scss';
import dropdown from '../../assets/icons/dropdown.svg';
import title from '../../assets/icons/title.svg';
import client from '../../assets/icons/client.svg';
import priority from '../../assets/icons/priority.svg';
import label from '../../assets/icons/label.svg';
import date from '../../assets/icons/date.svg';
import description from '../../assets/icons/description.svg';

class ViewModel {
  constructor() {
    this.dropdown = dropdown;
    this.title = title;
    this.client = client;
    this.priority = priority;
    this.label = label;
    this.date = date;
    this.description = description;
  }
}

ko.components.register('request-form', { viewModel: ViewModel, template });
