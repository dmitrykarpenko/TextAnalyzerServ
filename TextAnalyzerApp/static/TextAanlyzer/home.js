(function(){
    "use strict";

    angular.module("TextAnalyzer.demo", [])
        .controller("TextAnalyzerController",
            ['$scope', '$http', TextAnalyzerController]);

    function TextAnalyzerController($scope, $http) {
        $scope.addUserTexts = function(user, title, text) {
            user.userTexts.push({
                title: title,
                text: text
            });
        };

        $scope.homeNgModel = {
            users: [{
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
            }]
        };
    }
}());