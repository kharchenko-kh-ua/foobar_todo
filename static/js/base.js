/*jslint browser: true*/
/*global $, jQuery, alert, console*/
(function () {
    "use strict";

    $(document).on("ready", function () {

        //var $change_language_form = $("#change_language_form");
        //
        //$(".lang-choice").on("click", function () {
        //    $change_language_form.find("input[name=language]").val(this.id);
        //    $change_language_form.submit();
        //});

        String.prototype.format = function () {

            var args = arguments;
            return this.replace(/\{\{|\}\}|\{(\d+)\}/g, function (m, n) {
                if ("{{" === m) {
                    return "{";
                }
                if ("}}" === m) {
                    return "}";
                }
                return args[n];
            });
        };

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                function getCookie(name) {
                    var cookieValue = null, i, cookies, cookie;
                    if (document.cookie && document.cookie !== "") {
                        cookies = document.cookie.split(';');
                        for (i = 0; i < cookies.length; i++) {
                            cookie = jQuery.trim(cookies[i]);

                            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            }
        });
    });
}());