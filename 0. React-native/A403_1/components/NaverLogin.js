import React, { useEffect, useState } from 'react';
import { Button } from 'react-native';
import * as AuthSession from 'expo-auth-session';
import AsyncStorage from '@react-native-async-storage/async-storage';

const NAVER_CLIENT_ID = '839C3Xl5rNF_HFuT6zf7';
const NAVER_CLIENT_SECRET = 'j4ubhdXZY7';
const NAVER_REDIRECT_URI = AuthSession.makeRedirectUri({ scheme: 'A403' });

const discovery = {
  authorizationEndpoint: 'https://nid.naver.com/oauth2.0/authorize',
  tokenEndpoint: 'https://nid.naver.com/oauth2.0/token',
  revocationEndpoint: 'https://nid.naver.com/oauth2.0/token',
};

const NaverLogin = ({ onLoginSuccess }) => {
  const [userInfo, setUserInfo] = useState(null);
  
  const [request, response, promptAsync] = AuthSession.useAuthRequest(
    {
      clientId: NAVER_CLIENT_ID,
      redirectUri: NAVER_REDIRECT_URI,
      scopes: ['profile'],
      usePKCE: false,
    },
    discovery
  );

  useEffect(() => {
    const handleResponse = async () => {
      if (response?.type === 'success') {
        const tokenResponse = await fetch(
          `https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&client_id=${NAVER_CLIENT_ID}&client_secret=${NAVER_CLIENT_SECRET}&code=${response.params.code}&state=STATE_STRING`
        );
        const tokenData = await tokenResponse.json();
        const userResponse = await fetch('https://openapi.naver.com/v1/nid/me', {
          headers: {
            Authorization: `Bearer ${tokenData.access_token}`
          }
        });
        const userData = await userResponse.json();
        setUserInfo(userData.response);
        await AsyncStorage.setItem('naver_token', tokenData.access_token);
        onLoginSuccess(userData.response);
      }
    };

    handleResponse();
  }, [response]);

  useEffect(() => {
    const getToken = async () => {
      const token = await AsyncStorage.getItem('naver_token');
      if (token) {
        const userResponse = await fetch('https://openapi.naver.com/v1/nid/me', {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        const userData = await userResponse.json();
        setUserInfo(userData.response);
        onLoginSuccess(userData.response);
      }
    };
    getToken();
  }, []);

  return <Button disabled={!request} title="Login with Naver" onPress={() => promptAsync()} />;
};

export default NaverLogin;
