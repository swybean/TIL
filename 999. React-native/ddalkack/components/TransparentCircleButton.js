import React from "react";
import { View, Pressable, StyleSheet, Platform } from "react-native";
import { MaterialIcons } from "@expo/vector-icons";

function TransparentCircleButton({ name, color, hasMarginRight, onPress }) {
  return (
    <View
      style={[styles.iconButtonWrapper, hasMarginRight && styles.rightMargin]}
    >
      <Pressable
        style={({ pressed }) => [
          styles.iconButton,
          Platform.OS === "ios" &&
            pressed && {
              backgroundColor: "#efefef",
            },
        ]}
        onPress={onPress}
        android_ripple={{ color: "#ededed" }}
      >
        <MaterialIcons name={name} size={24} color={color} />
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  iconButtonWrapper: {
    width: 32,
    height: 32,
    borderRadius: 16,
    overflow: "hidden",
  },
  iconButton: {
    alignItems: "center",
    justifyContent: "center",
    width: 32,
    height: 32,
    borderRadius: 16,
  },

  rightMargin: {
    rightMargin: 8,
  },
});

export default TransparentCircleButton;
