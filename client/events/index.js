import $ from 'jquery';
import adjustCommentInput from './responsiveness';
import {
  DropdownAnimations,
  requestFormShowHide,
  sideStripSlide,
} from './animations';

// Sets up the different events for each lifecycle.
const setupEvents = () => {
  // Things to do when the page loads.
  $(window).on('load', () => {
    $('.request-form__container').click((event) => {
      event.stopPropagation();
    });

    adjustCommentInput();
    requestFormShowHide();
    sideStripSlide();

    new DropdownAnimations(
      '.request-list__dropdown-icon',
      '.request-list__day',
      '.request-list__entries',
    ).registerAnimations();

    new DropdownAnimations(
      '.request-details__description-top-bar > .request-details__dropdown-icon',
      '.request-details__description-container',
      '.request-details__description-text',
    ).registerAnimations(-90);

    new DropdownAnimations(
      '.request-details__comment-top-bar > .request-details__dropdown-icon',
      '.request-details__comment-container',
      '.request-details__comments',
    ).registerAnimations(-90);
  });

  // Things to do when window resizes.
  $(window).on('resize', () => {
    adjustCommentInput();
  });
};

export default setupEvents;
