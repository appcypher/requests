// Libraries
import ko from 'knockout';
// Components
import './components/view';

class ViewModel {
  constructor() {
    this.inputValue = ko.observable('Hello');
  }
}

ko.applyBindings(new ViewModel(), document.getElementById('app'));
