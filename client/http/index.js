import axios from 'axios';
import {
  requestsUrl,
  requestUrl,
  requestCommentsUrl,
  clientsUrl,
  staffUrl,
} from './urls';

const getStaff = id => axios.get(staffUrl(id));

const getClient = id => axios.get(clientsUrl(id));

const getRequest = id => axios.get(requestUrl(id));

const getRequests = () => axios.get(requestsUrl);

const postRequest = data => axios.post(requestsUrl, data);

const postRequestComment = (id, data) => axios.post(requestCommentsUrl(id), data);

export {
  getStaff,
  getClient,
  getRequests,
  getRequest,
  postRequest,
  postRequestComment,
};
