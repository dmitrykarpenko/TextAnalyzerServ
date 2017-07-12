(function(){
    "use strict";

    angular.module("TextAnalyzer.demo", [])
        .controller("TextAnalyzerController",
            ['$scope', '$http', TextAnalyzerController]);

    function TextAnalyzerController($scope, $http) {
        $scope.addUserTexts = function(user, title, text) {
            user.texts.push({
                title: title,
                text: text
            });
        };

        $scope.homeNgModel = {
            users: []
        };

        $http.get("/textanalyzerapp/users")
            .then(function(response) {
                $scope.homeNgModel.users = response.data;
            });
    }
}());