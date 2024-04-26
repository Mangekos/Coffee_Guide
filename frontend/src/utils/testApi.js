// const getResponseData = async res => {
// 	if (!res.ok) {
// 		const data = await res.json();
// 		throw new Error(data.message);
// 	}
// 	return res.json();
// };

// export function register(name, email, organization_inn) {
// 	return fetch('http://127.0.0.1:8000/api/v1/users/', {
// 		method: 'POST',
// 		headers: {
// 			Accept: 'application/json',
// 			'Content-Type': 'application/json',
// 		},
// 		body: JSON.stringify({ name, email, organization_inn }),
// 	}).then(res => {
// 		return getResponseData(res);
// 	});
// }
