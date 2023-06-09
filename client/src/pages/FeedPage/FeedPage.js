import { Container } from "@mui/material";
import Feed from "../../components/Feed/Feed";

const FeedPage = () => {
  return (
    <Container sx={{ display: "flex", justifyContent: "center", py: 2 }}>
      <Feed />
    </Container>
  );
};

export default FeedPage;
