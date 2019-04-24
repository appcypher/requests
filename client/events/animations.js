/* eslint-disable no-param-reassign */
import $ from 'jquery';
import Timer from './timer';


// Rotates an item by specified degrees.
const rotate = (target, degree, duration = 1) => {
  $(target).animate(
    { deg: `+=${degree}` },
    {
      duration: duration * 1000,
      step(deg) {
        $(target).css({ transform: `rotate(${deg}deg)` });
      },
    },
  );
};

// Performs the slide animation on targets.
const requestListDropdownAnimate = ({ trigger, toggle, target }, orientation = 90) => {
  $(trigger).click(() => {
    const requestList = target;

    if (toggle) {
      requestList.slideUp('fast');
      rotate(trigger, orientation, 0.3);
      toggle = false;
    } else {
      requestList.slideDown('fast');
      rotate(trigger, -orientation, 0.3);
      toggle = true;
    }
  });
};

// Slides the toast in and out.
const toastSlide = () => {
  const toast = $('.toast');
  const loader = $('.loader');
  const container = $('.popup-container');

  loader.hide();
  toast.css('display', 'flex');
  container.css('display', 'flex');

  toast.css({ left: '-500px' });
  toast.animate({ left: '20px' });

  setTimeout(() => {
    toast.animate({ left: '-500px' });

    setTimeout(() => {
      toast.css({ left: '0' });
      container.hide();
      toast.hide();
    }, 500);
  }, 2000);
};

// Shows the request form when add button is clicked
const requestFormShowHide = () => {
  // Show form on add button click.
  $('.request-list__add-button').click(() => {
    $('.request-form__background').css('display', 'flex');
  });

  // On form background click, hide input.
  $('.request-form__background').click(() => {
    $('.request-form__background').hide();
  });
};


// Slides the side strip on hover.
const sideStripSlide = () => {
  $('.sidebar__icon-container').mouseenter(() => {
    const sideStrip = $('.sidebar__side-strip');
    sideStrip.css({ left: '-5px' });
    sideStrip.animate({ left: '0' });
  });
};

// Details what should happen to suggestion box when typing.
const suggestionBoxEvents = (selector, timeout) => {
  // Hide suggestion when timeout runs up.
  const fn = () => {
    timeout = null;
    $(selector).hide();
  };

  if (!timeout) {
    timeout = new Timer(fn, 3000);
    $(selector).show();
  } else {
    timeout.extend(3000);
  }

  // Make sure suggestion box stay in focus when mouse is on list.
  $(selector).mouseenter(() => timeout && timeout.stop());
  $(selector).mouseleave(() => timeout && timeout.restart(3000));
};

/**
 * Class for managing request list dropdown animations.
 */
class DropdownAnimations {
  constructor(
    triggerSelector,
    triggerParentSelector,
    targetSelector,
  ) {
    this.dropdowns = []; // [{ trigger, toggle, target }]
    this.getDropdownTargets(
      triggerSelector,
      triggerParentSelector,
      targetSelector,
    );
  }

  // Gets all the dropdown targets in a request lists.
  getDropdownTargets(
    triggerSelector,
    triggerParentSelector,
    targetSelector,
  ) {
    $(triggerSelector).each((index, trigger) => {
      this.dropdowns.push({
        trigger,
        toggle: true,
        target: $(trigger)
          .parents(triggerParentSelector)
          .children(targetSelector),
      });
    });
  }

  // Registers cool animation on dropdown.
  registerAnimations(orientation = 90) {
    this.dropdowns.forEach((dropdown) => {
      requestListDropdownAnimate(dropdown, orientation);
    });
  }
}

export {
  DropdownAnimations,
  requestFormShowHide,
  sideStripSlide,
  toastSlide,
  suggestionBoxEvents,
};
