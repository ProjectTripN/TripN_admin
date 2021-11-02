import {
  configureStore,
  combineReducers, // redux의 그것과 같다.
  getDefaultMiddleware
} from "@reduxjs/toolkit";
import logger from 'redux-logger'
import counterReducer from 'features/counter/counterSlice';
import adminReducer from 'features/admin/reducers/adminSlice';

const rootReducer = combineReducers({ adminReducer })

export const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
});