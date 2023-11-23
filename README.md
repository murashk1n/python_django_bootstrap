# Route Search Website based on Given Parameters.

## Task:

Search for a route from one point to another. The task is divided into 3 parts - city, trains, and routes.

## Cities

Implement the addition, editing, deletion of a city, as well as paginated viewing of all available cities. A city has
only a name.

## Trains.

Implement the addition, editing, deletion of a train, as well as paginated viewing of all available trains. A train has
a unique code (name), the start of the route, the end of the route, and travel time in conditional units. There may be
several trains from one point to another, but they must differ in travel time.

## Routes.

The user selects the starting and ending point of the route, as well as specifies the maximum travel time. The user can
also add as many intermediate cities as desired, through which the route should pass. Routes that meet the conditions
are loaded for the user. Next to each route, there should be a button allowing the user to save the route by giving it a
name. When searching for routes, attention should be paid to the direction of train movement.

## Results Output.

The display of routes is sorted by the shortest travel time. That is, the route with the shortest travel time is
displayed first. The route description should contain information about where this route leads from and to, travel time,
as well as a list of all trains in this route with the train number, origin/destination, and travel time.
In case the route is not found, display the message: "No route satisfying the search conditions exists." If the
specified travel time is less than the minimum route time, then display the message: "Travel time is greater than the
time you selected. Please adjust the time."

## Saved Routes.

There should be a separate page for viewing saved routes. A route can only be saved, viewed, and deleted. Editing a
saved route is not allowed.

## Tests.

Tests should cover 40% of the code.

## Access to the Website.

Access to adding/editing Trains/Places, as well as deleting any records, should only be available to registered users.