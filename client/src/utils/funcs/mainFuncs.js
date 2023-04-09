import axios from "axios";


export const getFeedData = async (accessToken) => {
  try {
    if (await accessToken) {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/videos/main/",
        {
          Authorization: "Bearer " + accessToken,
        }
      );
      if (response.status < 300) {
        return await response.data.results;
      }
    } else {
      const response = await axios.get(
        "http://127.0.0.1:8000/api/v1/videos/main/"
      );
      if (response.status < 300) {
        return await response.data.results;
      }
    }
  } catch (error) {
    return false;
  }
};

export const isLiked = async (videoId, accessToken) => {
  try {
    const response = await axios.get(
      `http://127.0.0.1:8000/api/v1/videos/${videoId}/likes/0/`,
      {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }
    );
    if (response.status < 300) {
      return true;
    } else {
      return false;
    }
  } catch (error) {
    return false;
  }
};

export const videoLike = async (videoId, accessToken, remove) => {
  try {
    if (videoId && !remove) {
      const response = await axios.post(
        `http://127.0.0.1:8000/api/v1/videos/${videoId}/likes/`,
        {},
        {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );
      if (response < 300) {
        return response;
      } else {
        return false;
      }
    } else if (videoId && remove) {
      const response = await axios.delete(
        `http://127.0.0.1:8000/api/v1/videos/${videoId}/likes/0/`,
        {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        }
      );
      if (response < 300) {
        return response;
      } else {
        return false;
      }
    } else {
      return false;
    }
  } catch (error) {
    return false;
  }
};


