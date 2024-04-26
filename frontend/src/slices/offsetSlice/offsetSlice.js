import { createSlice } from '@reduxjs/toolkit';
import { useSelector } from 'react-redux';

const offsetSlice = createSlice({
	name: 'offset',
	initialState: 1,
	reducers: {
		increment: state => state + 1,
		reset: state => {
			state = 1;
		},
	},
});

export const { increment, reset } = offsetSlice.actions;
export default offsetSlice.reducer;
