/*
 * Copyright (C) 2019 Open Source Robotics Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
*/

#ifndef RMF_TRAFFIC__TEST__UNIT__SCHEDULE__UTILS_TRAJECTORY_HPP
#define RMF_TRAFFIC__TEST__UNIT__SCHEDULE__UTILS_TRAJECTORY_HPP

#include <rmf_traffic/DetectConflict.hpp>
#include <rmf_traffic/Trajectory.hpp>

//#include <rmf_traffic/geometry/Box.hpp>
#include <src/rmf_traffic/geometry/Box.hpp>

#include <rmf_traffic/geometry/Circle.hpp>
#include <rmf_traffic/schedule/Database.hpp>

#include <iostream>

#include <rmf_utils/catch.hpp>

//==============================================================================
inline bool check_equal_trajectory(
  const rmf_traffic::Trajectory& t1,
  const rmf_traffic::Trajectory& t2)
{
  REQUIRE(t1.size() == t2.size());
  REQUIRE(t1.start_time());
  REQUIRE(t1.finish_time());
  REQUIRE(t2.start_time());
  REQUIRE(t2.finish_time());

  auto t1_it = t1.begin();
  auto t2_it = t2.begin();

  bool test_passes = true;
  for (; t1_it != t1.end(); ++t1_it, ++t2_it)
  {
    const bool positions_match =
      (t1_it->position() - t2_it->position()).norm()
        == Approx(0.0).margin(1e-6);
    CHECK(positions_match);
    if (!positions_match)
    {
      std::cout << t1_it->position().transpose() << " vs\n"
                << t2_it->position().transpose() << std::endl;
    }

    const bool velocities_match =
      (t1_it->velocity() - t2_it->velocity()).norm()
        == Approx(0.0).margin(1e-6);
    CHECK(velocities_match);
    if (!velocities_match)
    {
      std::cout << t1_it->velocity().transpose() << " vs\n"
                << t2_it->velocity().transpose() << std::endl;
    }

    const bool times_match =
      (t1_it->time() - t2_it->time()).count() == Approx(0.0);
    CHECK(times_match);
    if (!times_match)
    {
      std::cout << t1_it->time().time_since_epoch().count() << " vs\n"
                << t2_it->time().time_since_epoch().count() << std::endl;
    }

    test_passes &= positions_match && velocities_match && times_match;
  }

  return test_passes;
}

inline bool check_trajectory_count(
  const rmf_traffic::schedule::Viewer& d,
  const std::size_t expected_participant_num,
  const std::size_t expected_trajectory_num)
{
  const auto view = d.query(rmf_traffic::schedule::query_all());
  const bool correct_trajectory_num = view.size() == expected_trajectory_num;
  CHECK(correct_trajectory_num);

  const bool correct_participant_num =
    d.participant_ids().size() == expected_participant_num;
  CHECK(correct_participant_num);

  return correct_trajectory_num && correct_participant_num;
}

#define CHECK_TRAJECTORY_COUNT( \
  d, expected_participant_num, expected_trajectory_num) \
  { \
    const bool trajectory_count_valid = check_trajectory_count( \
      d, expected_participant_num, expected_trajectory_num); \
    CHECK(trajectory_count_valid); \
  }

inline std::vector<rmf_traffic::Trajectory> get_conflicting_trajectories(
  const rmf_traffic::schedule::Viewer::View& view,
  const rmf_traffic::Profile& p,
  const rmf_traffic::Trajectory& t)
{
  std::vector<rmf_traffic::Trajectory> collision_trajectories;
  for (const auto& v : view)
  {
    const auto& v_p = v.description.profile();
    const auto& v_t = v.route->trajectory();
    if (rmf_traffic::DetectConflict::between(v_p, v_t, nullptr, p, t, nullptr))
      collision_trajectories.push_back(v_t);
  }

  return collision_trajectories;
}

//==============================================================================
using RouteId = rmf_traffic::RouteId;
using ConstRoutePtr = rmf_traffic::ConstRoutePtr;

//==============================================================================
inline bool check_itinerary(
  const rmf_traffic::schedule::Participant& p,
  const rmf_traffic::schedule::Database& db)
{
  const auto database_itinerary = db.get_itinerary(p.id());
  REQUIRE(database_itinerary.has_value());
  REQUIRE(p.itinerary().size() == database_itinerary->size());
  bool test_passed = true;
  for (std::size_t i = 0; i < p.itinerary().size(); ++i)
  {
    const auto& database_route = database_itinerary->at(i);
    const auto& participant_route = p.itinerary().at(i);

    const auto map_matches = database_route->map() == participant_route.map();
    CHECK(map_matches);

    const auto trajectory_matches = check_equal_trajectory(
      participant_route.trajectory(), database_route->trajectory());
    CHECK(trajectory_matches);

    test_passed &= map_matches && trajectory_matches;
  }

  return test_passed;
}

//==============================================================================
#define CHECK_ITINERARY(p, db) \
  { \
    const bool itinerary_valid = check_itinerary(p, db); \
    CHECK(itinerary_valid); \
  }

//==============================================================================
inline rmf_traffic::schedule::Itinerary create_test_input(
  const rmf_traffic::Trajectory& t)
{
  return {rmf_traffic::Route("test_map", t)};
}

#endif //RMF_TRAFFIC__TEST__UNIT__SCHEDULE__UTILS_TRAJECTORY_HPP
