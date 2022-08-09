function _dataApiKeydownHandler(event) {
  // If not input/textarea:
  //  - And not a key in REGEXP_KEYDOWN => not a dropdown command
  // If input/textarea:
  //  - If space key => not a dropdown command
  //  - If key is other than escape
  //    - If key is not up or down => not a dropdown command
  //    - If trigger inside the menu => not a dropdown command
  if (/input|textarea/i.test(event.target.tagName) ? event.which === SPACE_KEYCODE || event.which !== ESCAPE_KEYCODE && (event.which !== ARROW_DOWN_KEYCODE && event.which !== ARROW_UP_KEYCODE || $(event.target).closest(Selector$4.MENU).length) : !REGEXP_KEYDOWN.test(event.which)) {
    return;
  }

  event.preventDefault();
  event.stopPropagation();

  if (this.disabled || $(this).hasClass(ClassName$4.DISABLED)) {
    return;
  }

  var parent = Dropdown._getParentFromElement(this);

  var isActive = $(parent).hasClass(ClassName$4.SHOW);

  if (!isActive || isActive && (event.which === ESCAPE_KEYCODE || event.which === SPACE_KEYCODE)) {
    if (event.which === ESCAPE_KEYCODE) {
      var toggle = parent.querySelector(Selector$4.DATA_TOGGLE);
      $(toggle).trigger('focus');
    }

    $(this).trigger('click');
    return;
  }

  var items = [].slice.call(parent.querySelectorAll(Selector$4.VISIBLE_ITEMS));

  if (items.length === 0) {
    return;
  }

  var index = items.indexOf(event.target);

  if (event.which === ARROW_UP_KEYCODE && index > 0) {
    // Up
    index--;
  }

  if (event.which === ARROW_DOWN_KEYCODE && index < items.length - 1) {
    // Down
    index++;
  }

  if (index < 0) {
    index = 0;
  }

  items[index].focus();
}