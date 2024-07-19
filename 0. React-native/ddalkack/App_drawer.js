import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createDrawerNavigator } from "@react-navigation/drawer";
import { View, Text, Button } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

const Drawer = createDrawerNavigator();

function HomeScreen({ navigation }) {
  return (
    <View>
      <Text>Home</Text>
      <Button title="Drawer Open" onPress={() => navigation.openDrawer()} />
      <Button
        title="Setting Open"
        onPress={() => navigation.navigate("Setting")}
      />
    </View>
  );
}

function SettingScreen({ navigation }) {
  return (
    <View>
      <Text>setting</Text>
      <Button title="Back" onPress={() => navigation.goBack()} />
    </View>
  );
}

function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator
        initialRouteName="Home"
        drawerPosition="left"
        backBehavior="history"
        drawerContent={({ navigation }) => (
          <SafeAreaView>
            <Text>A Custom Drawer</Text>
            <Button
              onPress={() => navigation.closeDrawer()}
              title="Drawer 닫기"
            />
          </SafeAreaView>
        )}
      >
        <Drawer.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: "홈" }}
        />
        <Drawer.Screen
          name="Setting"
          component={SettingScreen}
          options={{ title: "설정" }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  );
}

export default App;
