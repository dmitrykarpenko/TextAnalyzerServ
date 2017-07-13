(function(){
    "use strict";

    angular.module("TextAnalyzer.demo", [])
        .controller("TextAnalyzerController",
            ['$scope', '$http', TextAnalyzerController]);

    function TextAnalyzerController($scope, $http) {
        $scope.addUserTexts = function(user, title, text) {
            var userText = {
                user: user.id,
                title: title,
                text: text
            };
            $http.post("/textanalyzerapp/usertexts/", userText)
                .then(function(response) {
                    user.texts.push(response.data);
                },
                function() {
                    alert("Couldn't create");
                });
        };

        $scope.homeNgModel = {
            users: []
        };

        $http.get("/textanalyzerapp/users/")
            .then(function(response) {
                $scope.homeNgModel.users = response.data;
            });
    }
}());