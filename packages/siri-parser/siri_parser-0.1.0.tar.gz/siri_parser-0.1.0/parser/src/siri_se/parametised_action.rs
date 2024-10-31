


#[derive(Debug)]
pub struct ParameterisedAction {
    pub action_status: Option<ActionStatus>,      // Optional status of the action
    pub description: Option<String>,               // Optional description of the action
    pub action_data: Vec<ActionData>,              // List of associated action data
}