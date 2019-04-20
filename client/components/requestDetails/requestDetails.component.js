import ko from 'knockout';
import $ from 'jquery';
import template from './requestDetails.html';
import './requestDetails.scss';
import description from '../../assets/icons/description.svg';
import comment from '../../assets/icons/comment.svg';
import dropdown from '../../assets/icons/dropdown.svg';

class ViewModel {
  constructor() {
    this.description = description;
    this.comment = comment;
    this.dropdown = dropdown;
  }
}

ko.components.register('request-details', { viewModel: ViewModel, template });
