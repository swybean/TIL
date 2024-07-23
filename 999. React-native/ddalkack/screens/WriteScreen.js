import { NavigationContainer } from "@react-navigation/native";
import React, { useState, useContext } from "react";
import { StyleSheet, View, KeyboardAvoidingView, Platform } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import WriteHeader from "../components/WriteHeader";
import WriteEditor from "../components/WriteEditor";
import { useNavigation } from "@react-navigation/native";
import LogContext from "../contexts/LogContext";

function WriteScreen() {
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const navigation = useNavigation();

  const { onCreate } = useContext(LogContext);

  const onSave = () => {
    onCreate({
      title,
      body,
      date: new Date().toISOString(),
    });
    navigation.pop();
  };

  return (
    <SafeAreaView style={stlyes.block}>
      <KeyboardAvoidingView style={stlyes.avoidingView}>
        <WriteHeader onSave={onSave} />
        <WriteEditor
          title={title}
          body={body}
          onChangeTitle={setTitle}
          onChangeBody={setBody}
        />
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const stlyes = StyleSheet.create({
  block: {
    flex: 1,
    backgroundColor: "white",
  },
  avoidingView: {
    flex: 1,
  },
});

export default WriteScreen;
