// For Login Process, For Logout Button.
// No Error Process, No Error code.
const Logout = async () => {
  const headers = new Headers();
  const formData = new FormData();
  const request = new Request('http://localhost:3001/unauth', {
    method: 'POST',
    headers: headers,
    body: formData,
    credentials: 'include',
  });
  let error = false
  await fetch(request)
  .then (response => {
    if (! response.ok) {
      error = true
    }
    return response.json();
  })
  .then (data => {
    if (error) {
      ;
    }
    return;
  })
  .catch (error => {
    return;
  });
  return;
}

export default Logout;
