(function(){
    "use strict";

    angular.module("TextAnalyzer.demo", [])
        .controller("TextAnalyzerController", ['$scope', TextAnalyzerController]);

    function TextAnalyzerController($scope) {
        $scope.addUserTexts = function(user, title, text) {
            user.userTexts.push({
                title: title,
                text: text
            });
        };

        $scope.homeNgModel = {
            user: {
                name: "Test user 1",
                userTexts: [
                    {
                        title: "Text 1 title",
                        text: "text 1"
                    },
                    {
                        title: "Text 2 title",
                        text: "text 2"
                    }
                ]
            }
        };
    }
}());