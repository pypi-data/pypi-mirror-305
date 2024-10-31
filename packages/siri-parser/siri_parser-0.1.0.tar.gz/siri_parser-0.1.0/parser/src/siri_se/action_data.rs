

#[derive(Debug)]
pub struct ActionData {
    pub name: String,                              // Name of the action
    pub prompt: Option<String>,                    // Optional message label associated with the publishing action
    pub publish_at_scope: Option<PublishAtScope>, // Optional scope for publishing the prompt
}