import ko from 'knockout';
import './components';
import setupEvents from './utilities/events';

setupEvents();

ko.applyBindings({}, document.getElementById('app'));
