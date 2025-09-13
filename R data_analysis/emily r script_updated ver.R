#從電腦讀檔案
emily <- read.csv(file.choose(), stringsAsFactors = FALSE, fileEncoding = "UTF-8")
names(emily) <- trimws(names(emily))  # 先移除空白
names(emily)[names(emily) == "Spreadsheet..test.items"] <- "item"

library(Rmisc)

emily$group <- ifelse(emily$mode == "machine", "group2",
                      ifelse(emily$mode == "BA Model", "group3", "group1"))

# 轉換必要欄位為 factor
groupvars <- c("BA", "mode", "Category", "group", "Participant")
for (col in groupvars) {
  if (col %in% names(emily)) {
    emily[[col]] <- as.factor(emily[[col]])
  } else {
    stop(paste0(col, " 欄位不存在！"))
  }
}

# 確保 Accuracy 是數值型別

library(writexl)
emily$Accuracy <- as.numeric(emily$Accuracy)

emilySE <- summarySE(data = emily,
                     measurevar = "Accuracy",
                     groupvars = c("BA", "mode", "Category"),
                     na.rm = TRUE)

emilySE_BA <- summarySE(data = emily,
                     measurevar = "Accuracy",
                     groupvars = c("BA", "mode"),
                     na.rm = TRUE)

emilySE_mode <- summarySE(data = emily,
                        measurevar = "Accuracy",
                        groupvars = ("mode"),
                        na.rm = TRUE)

print(emilySE)
print(emilySE_BA)
print(emilySE_mode)


write_xlsx(emilySE_BA, "emilySE_BA.xlsx")
write_xlsx(emilySE_mode, "emilySE_BA.xlsx")


# 篩選出 ChatGPT 模式下的資料
chatgpt_data <- subset(emily, mode == "ChatGPT")

ChatGPT_summary <- summarySE(data = chatgpt_data,
                             measurevar = "Accuracy",
                             groupvars = c("Category"),
                             na.rm = TRUE)

print(ChatGPT_summary)
write_xlsx(ChatGPT_summary, "aggregate_accuracy_ChatGPT_summary.xlsx")


# 篩選出 human 模式下的資料

human_data <- subset(emily, mode == "human")

human_summary <- summarySE(data = human_data,
                             measurevar = "Accuracy",
                             groupvars = c("Category"),  
                             na.rm = TRUE)

human_summary_BA <- summarySE(data = human_data,
                           measurevar = "Accuracy",
                           groupvars = "BA",  
                           na.rm = TRUE)

print(human_summary)
print(human_summary_BA)

write_xlsx(human_summary, "aggregate_accuracy_human_summary.xlsx")


# 篩選出 Ba model 模式下的資料

BA_Model_data <- subset(emily, mode == "BA Model")

BA_Model_summary <- summarySE(data = BA_Model_data,
                           measurevar = "Accuracy",
                           groupvars = c("Category"),  
                           na.rm = TRUE)

BA_Model_summary_BA <- summarySE(data = BA_Model_data,
                              measurevar = "Accuracy",
                              groupvars = "BA",  
                              na.rm = TRUE)


print(BA_Model_summary)
print(BA_Model_summary_BA)

write_xlsx(BA_Model_summary, "aggregate_accuracy_BA_Model_summary.xlsx")


emily$group <- ifelse(emily$mode == "machine", "group2",
                      ifelse(emily$mode == "BA Model", "group3", "group1"))


library(dplyr)

mode_accuracy <- emily %>%
  group_by(mode) %>%
  summarise(mean_accuracy = mean(Accuracy, na.rm = TRUE))

print(mode_accuracy)


library(ggplot2)
library(scales)
library(stringr)
library(forcats)
library(tidytext)


# 換行
emilySE <- emilySE %>%
  mutate(Category_wrapped = str_wrap(as.character(Category), width = 20))  # width = 每行最多 10 個字

category_order <- emilySE %>%
  group_by(Category) %>%
  summarise(mean_Accuracy = mean(Accuracy, na.rm = TRUE)) %>%
  arrange(desc(mean_Accuracy)) %>%
  pull(Category)

# 依照排序把 Category 變成 factor
emilySE$Category <- factor(emilySE$Category, levels = category_order)

# 重新設為 factor 並維持排序
emilySE$Category_wrapped <- factor(emilySE$Category_wrapped, 
                                   levels = str_wrap(levels(emilySE$Category), width = 20))

# 先計算每個 Category_wrapped 的平均 Accuracy（如果是你想用的依據）
category_order <- emilySE %>%
  group_by(Category_wrapped) %>%
  summarise(mean_acc = mean(Accuracy, na.rm = TRUE)) %>%
  arrange(mean_acc) %>%
  pull(Category_wrapped)

# 重新設定 Category_wrapped 的因子等級，依平均 Accuracy 排序
emilySE <- emilySE %>%
  mutate(Category_wrapped = factor(Category_wrapped, levels = category_order))

# 建立 ggplot
p <- ggplot(emilySE, aes(x = mode, y = Accuracy, fill = mode)) + 
  geom_bar(stat = "identity", position = position_dodge(width = 0.9), width = 0.7) +
  geom_errorbar(aes(ymin = Accuracy - ci, ymax = Accuracy + ci),
                width = 0.2, linewidth = 0.3,
                position = position_dodge(width = 0.9)) +
  geom_text(aes(label = scales::percent(Accuracy, accuracy = 1),
                y = Accuracy + ci + 0.02),
            position = position_dodge(width = 0.9),
            vjust = 0, size = 3) +
  facet_wrap(~ Category_wrapped, nrow = 2, scales = "free_x") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 9)) +
  labs(title = "Accuracy by Mode and Category",
       x = "Mode",
       y = "Accuracy") +
  coord_cartesian(ylim = c(0, 1.15)) +
  theme_minimal(base_size = 12) +
  theme(strip.text = element_text(size = 10),
        panel.spacing = unit(1, "lines"))
  

print(p)

#save plot to .png
ggsave("Accuracy_by_BA_Mode_Category.png", plot = p, width = 14, height = 8, dpi = 300)


library(lme4)
library(lmerTest)
library(ggeffects)

model=glm(Accuracy~BA, data=emily,family=binomial)
summary(model)

aggregate(Accuracy~BA*mode, emily, mean)


##run machine 20 times
m = glmer(Accuracy ~ BA * mode + (1|Participant) + (1|item), data = emily, 
          family = binomial, control = glmerControl(optimizer = "bobyqa"))


summary(m)

pred <- ggpredict(m, terms = c("BA", "mode"), bias_correction = TRUE)


aggregate(Accuracy ~ item * mode, emily, mean)

agg_result <- aggregate(Accuracy ~ item * mode, emily, mean)

write_xlsx(agg_result, "aggregate_accuracy_by_item_mode.xlsx")



mode_accuracy <- emily %>%
  group_by(mode) %>%
  summarise(mean_accuracy = mean(Accuracy, na.rm = TRUE))

print(mode_accuracy)




model=glm(Accuracy~BA, data=emily,family=binomial)
summary(model)

aggregate(Accuracy~BA*mode, emily, mean)


pred <- ggpredict(m, terms = c("BA", "mode"), bias_correction = TRUE)


aggregate(Accuracy ~ item * mode, emily, mean)

agg_result <- aggregate(Accuracy ~ item * mode, emily, mean)

write_xlsx(agg_result, "aggregate_accuracy_by_item_mode.xlsx")


# 篩選出 mode = "ChatGPT" 的資料
Chatgpt_data <- subset(emily, mode == "ChatGPT")
Human_data<- subset(emily, mode == "human")
BA_Model_data <- subset(emily, mode == "BA Model")

# 計算每個 Participant 在 ChatGPT mode 下的平均 Accuracy
accuracy_by_Chatgpt <- aggregate(Accuracy ~ Participant, data = Chatgpt_data, FUN = mean)
accuracy_by_human<- aggregate(Accuracy ~ Participant, data = human_data, FUN = mean)
accuracy_by_BA_Model<- aggregate(Accuracy ~ Participant, data = BA_Model_data, FUN = mean)

# 顯示結果
print(accuracy_by_Chatgpt)
print(accuracy_by_human)
print(accuracy_by_BA_Model)

write_xlsx(accuracy_by_Chatgpt, "aggregate_accuracy_by_participant_ChatGPT.xlsx")
write_xlsx(accuracy_by_human, "aggregate_accuracy_by_participant_Human.xlsx")
write_xlsx(accuracy_by_BA_Model, "aggregate_accuracy_by_participant_BA_Model.xlsx")

