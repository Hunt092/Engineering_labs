public ActionErrors validate(ActionMapping mapping, HttpServletRequest request) {
    ActionErrors errors = new ActionErrors();
    if (userName == null || userName.length() < 1) {
    errors.add("userName", new ActionMessage("error.userName.required"));
    }
    if (password == null || password.length() < 1) {
    errors.add("password", new ActionMessage("error.password.required"));
    }
    return errors;
    }


    public class LoginAction extends org.apache.struts.action.Action {
        private final static String SUCCESS = "success";
        private final static String FAILURE = "failure";
        public ActionForward execute(ActionMapping mapping, ActionForm form, HttpServletRequest request, HttpServletResponse response) throws Exception {
        LoginForm loginForm = (LoginForm) form;
        if (loginForm.getUserName().equals(loginForm.getPassword())) {
        return mapping.findForward(SUCCESS);
        } else {
        return mapping.findForward(FAILURE);
        }
        }
        }
        
    