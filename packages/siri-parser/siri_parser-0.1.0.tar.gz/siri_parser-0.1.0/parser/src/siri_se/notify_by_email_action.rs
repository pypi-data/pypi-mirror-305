

#[derive(Debug)]
pub struct NotifyByEmailAction {
    pub parameterized_action: Option<ParameterizedAction>,
    pub before_notices: Option<BeforeNotices>,
    pub clear_notice: Option<bool>,
    pub email: Option<String>,          // Email address for reminders
}