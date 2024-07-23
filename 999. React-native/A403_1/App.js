import React, { useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import NaverLogin from './components/NaverLogin';

const App = () => {
  const [userInfo, setUserInfo] = useState(null);

  const handleLoginSuccess = (user) => {
    setUserInfo(user);
  };

  return (
    <View style={styles.container}>
      {userInfo ? (
        <Text>Welcome, {userInfo.name}</Text>
      ) : (
        <View>
          <Text>Open up App.js to start working on your app!</Text>
          <NaverLogin onLoginSuccess={handleLoginSuccess} />
        </View>
      )}
      <StatusBar style="auto" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default App;
