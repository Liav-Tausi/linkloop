import { Box } from "@mui/material";
import { useContext } from "react";
import { AppContext } from "../../../App/AppStates/AppReducer";
import SearchRoundedIcon from "@mui/icons-material/SearchRounded";

const SearchBarSmallIcon = (props) => {
  const { themeMode, accessToken } = useContext(AppContext);
  return (
    <Box
      onClick={props.func}
      sx={{
        display: "flex",
        justifyContent: "center",
        py: accessToken ? "6px" : "5px",
        px: accessToken ? "6.5px" : "5.5px",
        borderRadius: "50%",
        backgroundColor: themeMode.searchBar,
        "&:hover": {
          backgroundColor: themeMode.navInputColor,
          cursor: "pointer",
        },
        "&:active": {
          transform: "scale(0.97)",
        },
      }}
    >
      <SearchRoundedIcon
        id={"SearchBar"}
        sx={{
          color: themeMode.textColor,
          fontSize: accessToken ? "24px" : "23px",
        }}
      />
    </Box>
  );
};

export default SearchBarSmallIcon;
