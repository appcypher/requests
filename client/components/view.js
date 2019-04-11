// Libraries
import ko from 'knockout';
// Templates
import template from './view.html';

class Product {
  constructor(name, rating) {
    this.name = name;
    this.userRating = ko.observable(rating || null);
  }
}

class ViewModel {
  constructor(params) {
    this.chosenValue = params.value;

    this.products = [
      new Product('Garlic bread'),
      new Product('Pain au chocolat'),
      new Product('Seagull spaghetti', 'like'), // This one was already 'liked'
    ];
  }
}

const viewModel = ViewModel;

ko.components.register('view', { viewModel, template });
