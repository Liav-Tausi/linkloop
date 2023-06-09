import { Box, Button, Container } from "@mui/material";
import Loading from "../../../utils/Comps/Loading";
import ScrollBar from "../../../utils/Comps/ScrollBar";
import { useContext, useState } from "react";
import {
  APP_ACTIONS,
  AppContext,
  AppDispatchContext,
} from "../../../App/AppStates/AppReducer";
import CloseRoundedIcon from "@mui/icons-material/CloseRounded";
import AddAPhotoIcon from "@mui/icons-material/AddAPhoto";
import { changeProfilePic } from "../../../utils/funcs/mainFuncs";
import SignSubmit from "../../NavBar/Menu/Sign/SignSubmit";

const ChangeProfilePicField = () => {
  const { themeMode, accessToken } = useContext(AppContext);
  const dispatch = useContext(AppDispatchContext);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState("");
  const [imgUrl, setImgUrl] = useState("");
  const [fileError, setFileError] = useState(false);

  const handleDeleteFile = () => {
    setFile("");
    setImgUrl("");
  };

  const handleChange = (event) => {
    const addedFile = event.target.files[0];
    if (addedFile.size > 5242880) {
      setFileError(true);
      setFile("");
    } else {
      setFileError(false);
      setFile(addedFile);
      setImgUrl(URL.createObjectURL(addedFile));
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    if (fileError) {
      setLoading(false);
      dispatch({
        type: APP_ACTIONS.MESSAGE,
        payload:
          "Please correct the errors in the form before submitting again.",
      });
    } else {
      const response = await changeProfilePic(accessToken, file);
      if (response) {
        setLoading(false);
        dispatch({
          type: APP_ACTIONS.MESSAGE,
          payload: "Picture Has Been Updated!",
        });
        dispatch({
          type: APP_ACTIONS.CHANGE_PROFILE_PIC,
        });
      } else {
        setLoading(false);
        dispatch({
          type: APP_ACTIONS.MESSAGE,
          payload: "ERROR! Picture Has Not Been Added!",
        });
      }
    }
  };


  const handleSubmitLinkLoopProd = async (event) => {
   event.preventDefault();
   alert("Sorry adding a profile pic to linkLoop is not allowed anymore for cloud space reasons.")
  };

  return (
    <>
      {loading && <Loading />}
      <Container style={{ borderRadius: "50px" }}>
        <ScrollBar maxHeight={"465px"}>
          <form onSubmit={handleSubmitLinkLoopProd}>
            {file === "" ? (
              <Button
                variant="contained"
                component="label"
                sx={{
                  borderRadius: "13px",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  p: 3,
                  flex: 1,
                  color: themeMode.textColor,
                  backgroundColor: themeMode.signUpFieldHover,
                  "&:hover": {
                    backgroundColor: themeMode.signUpField,
                  },
                }}
              >
                <AddAPhotoIcon
                  sx={{ color: themeMode.textColor, fontSize: 65 }}
                />
                <Box sx={{ textAlign: "center" }}>Choose a Profile Pic</Box>
                <input
                  hidden
                  type="file"
                  onChange={handleChange}
                  accept="image/*"
                  required
                />
              </Button>
            ) : (
              <Box
                sx={{
                  mt: 2,
                  display: "flex",
                  justifyContent: "center",
                  flexDirection: "column",
                }}
              >
                <Box
                  sx={{
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    position: "relative",
                    border:
                      "7px solid" +
                      (fileError
                        ? themeMode.appTheme
                        : themeMode.signUpFieldHover),
                  }}
                >
                  <img
                    alt="profile pic"
                    src={imgUrl}
                    style={{
                      width: "100%",
                      height: "100%",
                    }}
                    controls
                    required
                  />
                  <Box
                    onClick={handleDeleteFile}
                    sx={{
                      display: loading ? "none" : "flex",
                      justifyContent: "center",
                      alignItems: "center",
                      borderRadius: "50%",
                      position: "absolute",
                      top: 5,
                      right: 5,
                      zIndex: 9999,
                      px: 0.7,
                      py: 0.7,
                      backgroundColor: themeMode.navInputColor,
                      "&:hover": {
                        backgroundColor: themeMode.navInputColorHover,
                        cursor: "pointer",
                      },
                      "&:active": {
                        transform: "scale(0.98)",
                      },
                    }}
                  >
                    <CloseRoundedIcon
                      sx={{
                        transform: "scale(1.2)",
                        color: themeMode.textColor,
                      }}
                    />
                  </Box>
                </Box>
              </Box>
            )}
            <Box
              sx={{
                position: "absolute",
                display: "flex",
                justifyContent: "center",
                bottom: 22,
                left: "50%",
                right: "50%",
              }}
            >
              <SignSubmit />
            </Box>
          </form>
        </ScrollBar>
      </Container>
    </>
  );
};

export default ChangeProfilePicField;
