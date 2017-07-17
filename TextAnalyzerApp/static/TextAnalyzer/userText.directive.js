(function() {
    "use strict";

    angular.module("TextAnalyzer.demo")
        .directive("textAnalyzerUserText", UserTextDirective);

    function UserTextDirective() {
        return {
            templateUrl: "/static/TextAnalyzer/userText.html",
            restrict: "E"
        };
    }
})();