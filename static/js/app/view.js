(function ($) {
AppView = Backbone.View.extend({
  el: $("body"),
  events: {
    "click #ask-me":  "showPrompt",
  },
  showPrompt: function () {
    var question = alert("Want to know who your Daddy is?");
    $("#answers").append("<li>James Yeh</li>");
  }
});
var app_view = new AppView();
})(jQuery);
