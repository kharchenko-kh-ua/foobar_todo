/*jslint browser: true*/
/*global $, jQuery, alert, console*/
(function () {
    "use strict";

    $(document).on("ready", function () {
        var $trs = $("tr"), i, sorted = false,
            $formset = $("#formset");

        function makePositions() {
            for (i = 0; i < $trs.length; i++) {
                $("#id_form-" + i + "-sequence_number").val(i + 1);
            }
        }

        function remakePositions() {
            $("input[data-name='sequence_number']").each(function (index) {
                $(this).val(index + 1);
            });
        }

        function onFormSuccess() {
            sorted = false;
        }

        function formSubmit (e) {
            if (sorted === true) {
                var requestData = {
                    url: ".",
                    type: "POST",
                    data: new FormData(this),
                    processData: false,
                    contentType: false
                };
                var request = $.ajax(requestData);
                request.success(onFormSuccess);
                e.preventDefault();
                return false;
            }
        }
        makePositions();

        $formset.on("submit", formSubmit);

        $("#formset_table > tbody").sortable({
            change: function (event, ui) {
                sorted = true;
            },
            update: function (event, ui) {
                remakePositions();
                $formset.submit();
            }
        });
    });
}());
