

#[derive(Debug)]
pub struct Blocking {
    /// Indicates whether the event data should be considered by a journey planner.
    journey_planner: Option<bool>, // 0:1
}