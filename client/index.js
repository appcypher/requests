import ko from 'knockout';
import './components';
import setupEvents from './events';

setupEvents();

ko.applyBindings({}, document.getElementById('app'));
