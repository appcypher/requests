import $ from 'jquery';

const adjustCommentInput = () => {
  const newWidth = $('.request-details__content').width();
  $('.request-details__input-container').width(newWidth - 40);
};

export default adjustCommentInput;
