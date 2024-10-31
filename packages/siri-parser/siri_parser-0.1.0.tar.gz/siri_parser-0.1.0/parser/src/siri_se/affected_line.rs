

#[derive(Debug)]
pub struct AffectedLine {
    pub line_ref: LineRef,                    // Reference to the impacted line
    pub destinations: Vec<Destination>,        // List of affected destinations
    pub affected_stop_point: Option<AffectedStopPoint>, // Optional impacted stop point
    pub directions: Vec<Direction>,            // List of impacted directions
}