import { AppBar, Toolbar } from "@mui/material";
import { useContext, useEffect } from "react";
import Menu from "./Menu/Menu";
import Logo from "./Logo/Logo";
import { AppContext } from "../../App/AppStates/AppReducer";
import AppMessage from "../../App/MainApp/AppMessage/AppMessage";
import SearchBar from "./SearchBar/SearchBar";

const NavBar = () => {
  const { themeMode, message } = useContext(AppContext);

  useEffect(() => {
    console.log("nav refresh");
  }, []);

  return (
    <>
      <AppBar
        id="app"
        position="sticky"
        sx={{
          top: -1,
          backgroundColor: themeMode.navColor,
          borderBottom: "2px solid " + themeMode.navInputColor,
        }}
      >
        <Toolbar
          variant={"dense"}
          sx={{
            justifyContent: "space-between",
            "@media (max-width: 850px)": {
              px: 3,
            },
            "@media (max-width: 600px)": {
              px: 2,
            },
            "@media (max-width: 500px)": {
              px: 0,
            },
          }}
        >
          <Logo />
          <SearchBar />
          <Menu />
        </Toolbar>
      </AppBar>
      {message && <AppMessage />}
    </>
  );
};

export default NavBar;
