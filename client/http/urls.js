let baseUrl = 'http://localhost:5000/api/v1';

if (process.env.NODE_ENV && process.env.NODE_ENV === 'development') {
  baseUrl = 'http://localhost:5000/api/v1';
}

const requestsUrl = `${baseUrl}/requests`;
const requestUrl = id => `${baseUrl}/requests/${id}`;
const requestCommentsUrl = id => `${baseUrl}/requests/${id}/comments`;
const clientsUrl = id => `${baseUrl}/clients/${id}`;
const staffUrl = id => `${baseUrl}/staff/${id}`;

export {
  requestsUrl,
  requestUrl,
  requestCommentsUrl,
  clientsUrl,
  staffUrl,
};
