import $ from 'jquery';
import adjustCommentInput from './responsiveness';

const setupEvents = () => {
  // Things to make sure of when the page loads.
  $(document).ready(() => {
    adjustCommentInput();
  });

  // Things to do when window resizes.
  $(window).on('resize', () => {
    adjustCommentInput();
  });
};

export default setupEvents;
