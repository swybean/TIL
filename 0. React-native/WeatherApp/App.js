import React from "react";
import { AppRegistry, StyleSheet, Text, View } from "react-native";
import { StatusBar } from "expo-status-bar";

const App = () => {
  return (
    <View style={{ flex: 1, flexDirection: "row" }}>
      <View style={{ flex: 1, backgroundColor: "tomato" }}></View>
      <View
        style={{
          flex: 4,
          backgroundColor: "teal",
          justifyContent: "flex-start",
          alignItems: "center",
        }}
      >
        <Text
          style={{
            fontSize: 50,
            fontWeight: "bold",
            color: "white",
          }}
        >
          연습중
        </Text>
      </View>
      <View style={{ flex: 1, backgroundColor: "orange" }}></View>
      <StatusBar></StatusBar>
    </View>
  );
};

const styles = StyleSheet.create({});

AppRegistry.registerComponent("main", () => App);

export default App;
