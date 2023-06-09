import { useMediaQuery }  from "@mui/material";
import { createContext, useReducer, useRef } from "react";
import DARK_THEME from "../../assets/themes/DarkTheme";
import LIGHT_THEME from "../../assets/themes/LightTheme";
import { isLoggedIn } from "../../utils/funcs/authFuncs";
import { detectColorScheme } from "../../utils/funcs/confFuncs";

const awaitIsLoggedIn = async () => {
  return await isLoggedIn("");
};

export const INITIAL_APP_STATE = {
  accessToken: awaitIsLoggedIn(),
  connectedUser: null,
  themeMode: localStorage.getItem("preferredTheme")
    ? localStorage.getItem("preferredTheme") === "2"
      ? DARK_THEME
      : LIGHT_THEME
    : detectColorScheme() === "dark"
    ? DARK_THEME
    : LIGHT_THEME,
  message: null,
  forceThemeMode: localStorage.getItem("preferredTheme")
    ? localStorage.getItem("preferredTheme") === "2"
      ? 2
      : 1
    : 3,
  notImplemented: false,
  appLoaded: false,
  menuOpen: false,
  signUpOpen: false,
  signInOpen: false,
  userProfileData: "",
  profilePatch: false,
  changeProfilePic: false,
  addVideo: false,
  shareVideo: false,
  chooseLocation: false,
  searchBar: false,
};

export const APP_ACTIONS = {
  APP_LOADED: "appLoaded",
  ACCESS_TOKEN: "accessToken",
  MESSAGE: "message",
  THEME_MODE: "themeMode",
  FORCE_THEME_MODE: "forceThemeMode",
  MENU_OPEN_CLOSE: "openClose",
  SIGN_UP_OPEN: "signUpOpen",
  SIGN_IN_OPEN: "signInOpen",
  PROFILE_PATCH: "profilePatch",
  NOT_IMPLEMENTED: "notImplemented",
  CHANGE_PROFILE_PIC: "changeProfilePic",
  ADD_VIDEO: "addVideo",
  SHARE_VIDEO: "shareVideo",
  CHOOSE_LOCATION: "chooseLocation",
  CONNECTED_USER: "connectedUser",
  SEARCH_BAR: "searchBar",
};

export const AppReducer = (states, action) => {
  switch (action.type) {
    case APP_ACTIONS.ACCESS_TOKEN: {
      return {
        ...states,
        accessToken: action.payload,
      };
    }
    case APP_ACTIONS.CONNECTED_USER: {
      return {
        ...states,
        connectedUser: action.payload,
      };
    }
    case APP_ACTIONS.SEARCH_BAR: {
      return {
        ...states,
        searchBar: !states.searchBar,
      };
    }
    case APP_ACTIONS.MESSAGE: {
      return {
        ...states,
        message: action.payload,
      };
    }
    case APP_ACTIONS.MENU_OPEN_CLOSE: {
      return {
        ...states,
        menuOpen: !states.menuOpen,
      };
    }
    case APP_ACTIONS.SIGN_UP_OPEN: {
      return {
        ...states,
        signInOpen: false,
        signUpOpen: !states.signUpOpen,
      };
    }
    case APP_ACTIONS.SIGN_IN_OPEN: {
      return {
        ...states,
        signUpOpen: false,
        signInOpen: !states.signInOpen,
      };
    }
    case APP_ACTIONS.PROFILE_PATCH: {
      return {
        ...states,
        profilePatch: !states.profilePatch,
      };
    }
    case APP_ACTIONS.CHANGE_PROFILE_PIC: {
      return {
        ...states,
        changeProfilePic: !states.changeProfilePic,
      };
    }
    case APP_ACTIONS.NOT_IMPLEMENTED: {
      return {
        ...states,
        notImplemented: !states.notImplemented,
      };
    }
    case APP_ACTIONS.ADD_VIDEO: {
      return {
        ...states,
        addVideo: !states.addVideo,
      };
    }
    case APP_ACTIONS.SHARE_VIDEO: {
      return {
        ...states,
        shareVideo: !states.shareVideo,
      };
    }
    case APP_ACTIONS.CHOOSE_LOCATION: {
      return {
        ...states,
        chooseLocation: !states.chooseLocation,
      };
    }
    case APP_ACTIONS.THEME_MODE: {
      return {
        ...states,
        themeMode: action.payload,
      };
    }
    case APP_ACTIONS.FORCE_THEME_MODE: {
      return {
        ...states,
        forceThemeMode: action.payload,
      };
    }
    case APP_ACTIONS.APP_LOADED: {
      return {
        ...states,
        appLoaded: !states.appLoaded,
      };
    }

    default:
      throw new Error(`Unsupported action type: ${action.type}`);
  }
};

export const AppContext = createContext(INITIAL_APP_STATE);

export const AppDispatchContext = createContext(null);

export const IsSmallScreenContext = createContext(null);

export const Ref = createContext(null);

export const AppProvider = ({ children }) => {
  const [appState, dispatch] = useReducer(AppReducer, INITIAL_APP_STATE);
  const isSmallScreen = useMediaQuery("(max-width:600px)");
  const ref = useRef(null);

  return (
    <Ref.Provider value={ref}>
      <IsSmallScreenContext.Provider value={isSmallScreen}>
        <AppContext.Provider value={appState}>
          <AppDispatchContext.Provider value={dispatch}>
            {children}
          </AppDispatchContext.Provider>
        </AppContext.Provider>
      </IsSmallScreenContext.Provider>
    </Ref.Provider>
  );
};
