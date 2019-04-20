import ko from 'knockout';
import template from './requestList.html';
import './requestList.scss';
import search from '../../assets/icons/search.svg';
import dropdown from '../../assets/icons/dropdown.svg';
import check from '../../assets/icons/check.svg';
import plus from '../../assets/icons/plus.svg';

class ViewModel {
  constructor() {
    this.search = search;
    this.dropdown = dropdown;
    this.check = check;
    this.plus = plus;
  }
}

ko.components.register('request-list', { viewModel: ViewModel, template });
