import React from "react";
import { AppRegistry, StyleSheet, Text, View } from "react-native";
import { StatusBar } from "expo-status-bar";

const App = () => {
  return (
    <View style={{ flex: 1 }}>
      <View style={{ flex: 1, flexDirection: "row" }}>
        <View style={{ flex: 1, backgroundColor: "tomato" }}></View>
        <View
          style={{
            flex: 4,
            backgroundColor: "teal",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Text
            style={{
              fontSize: 40,
              fontWeight: "bold",
              color: "red",
            }}
          >
            난 첫번째 뷰!
          </Text>
        </View>
        <View style={{ flex: 1, backgroundColor: "orange" }}></View>
      </View>

      <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
        <Text style={{ color: "black", fontSize: 40, fontWeight: "bold" }}>
          안녕 난 2번째 뷰야
        </Text>
      </View>

      <View
        style={{
          flex: 1,
          justifyContent: "center",
          alignItems: "center",
          backgroundColor: "black",
        }}
      >
        <Text style={{ fontSize: 40, fontWeight: "bold", color: "white" }}>
          그럼 난 3번째 뷰!
        </Text>
      </View>

      <View
        style={{
          flex: 1,
          justifyContent: "center",
          alignItems: "center",
          backgroundColor: "red",
        }}
      >
        <Text style={{ fontSize: 40, fontWeight: "bold", color: "yellow" }}>
          그럼 난 4번째 뷰!
        </Text>
      </View>

      <View
        style={{
          flex: 1,
          justifyContent: "center",
          alignItems: "center",
          backgroundColor: "blue",
        }}
      >
        <Text style={{ fontSize: 40, fontWeight: "bold", color: "white" }}>
          그럼 난 5번째 뷰!
        </Text>
      </View>

      <View
        style={{
          flex: 1,
          justifyContent: "center",
          alignItems: "center",
          backgroundColor: "green",
        }}
      >
        <Text style={{ fontSize: 40, fontWeight: "bold", color: "black" }}>
          그럼 난 6번째 뷰!
        </Text>
      </View>

      <View
        style={{
          flex: 1,
          justifyContent: "center",
          alignItems: "center",
          backgroundColor: "yellow",
        }}
      >
        <Text style={{ fontSize: 40, fontWeight: "bold", color: "blue" }}>
          럭키세븐!!!!!!!
        </Text>
      </View>

      <StatusBar></StatusBar>
    </View>
  );
};

const styles = StyleSheet.create({});

AppRegistry.registerComponent("main", () => App);

export default App;
