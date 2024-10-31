


#[derive(Debug)]
pub struct NotifyBySmsAction {
    pub parameterized_action: Option<ParameterizedAction>,
    pub before_notices: Option<BeforeNotices>,
    pub clear_notice: Option<bool>,
    pub phone: Option<String>,           // Phone number for reminders
    pub premium: Option<bool>,           // Defaults to false
}